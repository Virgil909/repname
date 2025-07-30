from itertools import groupby

from flask import Flask, render_template
import pandas as pd
from sqlalchemy import create_engine
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import os

import dash_bootstrap_components as dbc
from sqlalchemy.dialects.mssql.information_schema import columns

# ----------ZONA INITIALIZARE QUERY-------------------------

priority_query = '''Select COUNT(PRIORITY), priority
                    From jira_snapshot
                    Where issue_type = 'Problem Report'  {aditional_filter}
                      AND _is_current = 'true'
                    Group by priority '''

status_query = '''Select COUNT(jira_status), jira_status
                  From jira_snapshot 
                  Where issue_type = 'Problem Report' {aditional_filter}
                  Group by jira_status

               '''

severity_query = '''Select COUNT(severity), severity
                    From jira_snapshot 
                    Where issue_type = 'Problem Report'{aditional_filter}
                    Group by severity 

                 '''

pivot_query = '''
    SELECT jira_status AS "Status", priority
    FROM jira_snapshot
    WHERE issue_type = 'Problem Report' {aditional_filter}
   
'''

feature_status_query='''
SELECT 
    COUNT(*) AS count,
    CASE 
        WHEN jira_status IN ('In Progress', 'In Review') THEN 'In Progress'
        ELSE jira_status
    END AS jira_status
FROM jira_snapshot
WHERE issue_type = 'Story' {aditional_filter}
GROUP BY jira_status
'''

crd_query='''WITH crd_status AS (
    SELECT
        c.id AS crd_id,
        CASE 
            WHEN COUNT(s.id) FILTER (WHERE s.syrd_state IS NOT NULL) > 0 
                 AND COUNT(s.id) FILTER (WHERE s.syrd_state <> 'Released') = 0
            THEN 'Implemented'
            ELSE 'Not_Implemented'
        END AS status
    FROM crd c
    LEFT JOIN syrd s ON c.id = s.crd_id
    WHERE 1=1 {aditional_filter}  
    GROUP BY c.id
)
SELECT status, COUNT(*)
FROM crd_status
GROUP BY status;
'''

requir_testcase_query='''
WITH syra_status AS (
    SELECT
        c.id AS syrd_id ,
        CASE 
            WHEN COUNT(t.id) FILTER (WHERE t.verdict IS NOT NULL) > 0 
                 AND COUNT(t.id) FILTER (WHERE t.verdict <> 'Passed') = 0
            THEN 'With Test Case'
            ELSE 'Without Test Case'
        END AS status
    FROM syrd c
    LEFT JOIN testcase t ON c.id = t.syrd_id
     WHERE 1=1 {aditional_filter}  
    GROUP BY c.id
)
SELECT status, COUNT(*)
FROM syra_status
GROUP BY status;
'''

requ_status_query='''
 Select Count(syrd_state),syrd_state
 From syrd c
WHERE 1=1 {aditional_filter}
 group by syrd_state
'''




dropdown_query = '''Select distinct agile_team
                    FROM jira_snapshot'''

dropdown_configs = [
    {
        "id": "agile_team_dropdown",
        "label": "Selectează echipa:",
        "query": "SELECT DISTINCT agile_team FROM jira_snapshot"
    },

]
dropdown_traceability_configs = [
    {
        "id": "test_level_dropdown",
        "label": "Selectează test:",
        "query": "SELECT DISTINCT test_level FROM crd"
    },
    {
        "id": "requirement_level_dropdown",
        "label": "Selectează requirement:",
        "query": "SELECT DISTINCT requirement_level FROM crd"
    }

]

list_call = [dropdown["id"] for dropdown in dropdown_configs]


common_dropdowns = ['agile_team_dropdown']
syrd_dropdowns = ['test_level_dropdown','requirement_level_dropdown']

priority_input = {
    'query': priority_query,
    'id_graph': 'the_graph',
    'up_val': 'count',
    'up_tit': 'Open PRs by Priority',
    'up_names': 'priority',
    'up_height': 500,
    'up_width': 500,
    'hole': 0.3,

    'filter_dropdown_ids': common_dropdowns
}

status_input = {
    'query': status_query,
    'id_graph': 'the_graph2',
    'up_val': 'count',
    'up_tit': 'Problem reports by Status',
    'up_names': 'jira_status',
    'up_height': 500,
    'up_width': 500,
    'hole': 0.3,
    'filter_dropdown_ids': common_dropdowns

}

severity_input = {
    'query': severity_query,
    'id_graph': 'the_graph3',
    'up_val': 'count',
    'up_tit': 'Open PRs by Severity',
    'up_names': 'severity',
    'up_height': 500,
    'up_width': 500,
    'hole': 0.3,
    'filter_dropdown_ids': common_dropdowns
}

table_input = {
    'query': pivot_query,
    'index_col': 'Status',
    'columns_col': 'priority',

}

feature_status_input = {
    'query': feature_status_query,
    'id_graph': 'the_graph4',
    'up_val': 'count',
    'up_tit': 'Feature Status',
    'up_names': 'jira_status',
    'up_height': 500,
    'up_width': 500,
    'hole': 0.3,
    'filter_dropdown_ids': common_dropdowns

}
crd_input = {
    'query': crd_query,
    'id_graph': 'the_graphcrd',
    'up_val': 'count',
    'up_tit': 'CRD Requirements Implemented in Software',
    'up_names': 'status',
    'up_height': 535,
    'up_width': 535,
    'hole': 0.3,
    'color_scheme': ['green','orange'],
    'filter_dropdown_ids': syrd_dropdowns
}

require_input={
'query': requir_testcase_query,
    'id_graph': 'the_graphreq',
    'up_val': 'count',
    'up_tit': 'Sys+Sw Requirements with Test Cases',
    'up_names': 'status',
    'up_height': 535,
    'up_width': 535,
    'hole': 0.3,
    'color_scheme': ['green','orange'],
    'filter_dropdown_ids': syrd_dropdowns
}
require_stats_input={
'query': requ_status_query,
    'id_graph': 'the_graphreqstats',
    'up_val': 'count',
    'up_tit': 'SyRD Requirement Status',
    'up_names': 'syrd_state',
    'up_height': 535,
    'up_width': 535,
    'hole': 0.3,
    'color_scheme': ['blue','red','purple','cyan'],
    'filter_dropdown_ids': syrd_dropdowns
}
