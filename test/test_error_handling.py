#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Jan 14, 2025

@author: mpechter

"""

from scripts.vippy.error_handler import (
    check_if_tag_field,
    get_error_condition,
    construct_error_statement_string,
    construct_error_statement_from_policy,
    construct_default_error_statement_for_required_items,
    has_custom_error,
    has_error_policy,
)


class TestErrorsWithPolicies:

    def test_check_if_tag_field(self):
        all_types = {}
        tag_data = {"type": "type1"}
        assert check_if_tag_field(all_types, tag_data) == True

    def test_get_error_condition(self):

        assert get_error_condition(True, True) == "the field is invalid,"
        assert (
            get_error_condition(False, False)
            == "the element is invalid or not present,"
        )

    def test_construct_error_statement_string(self):

        assert (
            construct_error_statement_string("the field is invalid,", "it")
            == "If the field is invalid, then it"
        )

    def test_construct_error_statement_from_policy(self):

        tag_data = {"containing_type": "type1"}
        error_policy = "=must-ignore"
        is_required = True
        is_tag_field = True
        assert (
            construct_error_statement_from_policy(
                tag_data, error_policy, is_required, is_tag_field
            )
            == "If the field is invalid, then the implementation is required to ignore it."
        )

    def test_construct_error_statement_from_policy(self):

        tag_data = {"containing_type": "type1"}
        error_policy = "=must-ignore"
        is_required = False
        is_tag_field = False
        assert (
            construct_error_statement_from_policy(
                tag_data, error_policy, is_required, is_tag_field
            )
            == "If the element is invalid or not present, then the implementation is required to ignore it."
        )
