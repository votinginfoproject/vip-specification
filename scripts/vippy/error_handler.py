#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Jan 13, 2025

@author: mpechter

"""

from pprint import pformat

CUSTOM_ERROR = "error"
TYPE = "type"
ERROR_POLICY = "error_then"
REQUIRED = "required"
ERROR_HANDLING = "error_handling"
ERROR_EXTRA = "error_extra"
ERROR_RESULT_STRING = "the implementation {action} ignore {ignore}."
ERROR_RESULT_FORMAT_FOR_REQUIRED_ITEMS = ERROR_RESULT_STRING.format(
    action="is required to", ignore="the ``{containing_type}`` element containing it"
)
ERROR_RESULT_OBJ = {
    "=must-ignore": ERROR_RESULT_STRING.format(action="is required to", ignore="it"),
    "=should-ignore": ERROR_RESULT_STRING.format(action="should", ignore="it"),
}


def check_if_tag_field(all_types: dict, tag_data: dict) -> bool:
    type_name = tag_data[TYPE]
    data_type = all_types.get(type_name)
    if data_type is None:
        return True
    else:
        return data_type.is_enum


def get_error_condition(is_required: bool, is_tag_field: bool) -> str:
    noun = "field" if is_tag_field else "element"
    condition = "invalid" if is_required else "invalid or not present"
    return f"the {noun} is {condition},"


def construct_error_statement_string(error_condition: str, error_result: str) -> str:
    return f"If {error_condition} then {error_result}"


def construct_error_statement_from_policy(
    tag_data: dict, error_policy: str, is_required: bool, is_tag_field: bool
) -> str:
    if not error_policy.startswith("="):
        raise ValueError("error policy must start with '='")
    error_condition = get_error_condition(is_required, is_tag_field)
    error_result_format = ERROR_RESULT_OBJ[error_policy]
    containing_type = tag_data["containing_type"]
    error_result = error_result_format.format(containing_type=containing_type)
    error_statement = construct_error_statement_string(error_condition, error_result)
    return error_statement


def construct_default_error_statement_for_required_items(
    tag_data: dict, is_required: bool, is_tag_field: bool
) -> str:
    error_condition = get_error_condition(is_required, is_tag_field)
    error_result = ERROR_RESULT_FORMAT_FOR_REQUIRED_ITEMS.format(**tag_data)
    error_statement = construct_error_statement_string(error_condition, error_result)
    return error_statement


def has_custom_error(tag_data: dict) -> bool:
    return CUSTOM_ERROR in tag_data


def has_error_policy(tag_data: dict) -> bool:
    return ERROR_POLICY in tag_data


def get_error_statement(tag_data: dict, is_required: bool, is_tag_field: bool) -> str:

    if has_custom_error(tag_data):
        error_statement = tag_data[CUSTOM_ERROR]
    elif has_error_policy(tag_data):
        error_policy = tag_data[ERROR_POLICY]
        error_statement = construct_error_statement_from_policy(
            tag_data, error_policy, is_required, is_tag_field
        )
    else:
        if not is_required:
            raise Exception(
                'we have not defined a default "error" value for '
                "tags that are not required.\n"
                f"tag data:\n{pformat(tag_data)}"
            )
        error_statement = construct_default_error_statement_for_required_items(
            tag_data, is_required, is_tag_field
        )

    return error_statement


def get_complete_error_statement(
    all_types: dict, tag_data: dict, is_required: bool
) -> str:
    is_tag_field = check_if_tag_field(all_types, tag_data)
    error_statement = get_error_statement(tag_data, is_required, is_tag_field)
    error_statement += tag_data.get(ERROR_EXTRA, "")

    return error_statement
