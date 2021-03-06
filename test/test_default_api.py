# coding: utf-8

"""
    Sensor Data API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import sensor_cloud
from sensor_cloud.rest import ApiException
from sensor_cloud.apis.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """ DefaultApi unit test stubs """

    def setUp(self):
        self.api = sensor_cloud.apis.default_api.DefaultApi()

    def tearDown(self):
        pass

    def test_aggregation_get(self):
        """
        Test case for aggregation_get

        Calculate an aggregated view of observations.
        """
        pass

    def test_collections_collectionid_shares_get(self):
        """
        Test case for collections_collectionid_shares_get

        Get shares for a collection
        """
        pass

    def test_collections_collectionid_shares_id_delete(self):
        """
        Test case for collections_collectionid_shares_id_delete

        Delete a share from an existing collection.
        """
        pass

    def test_collections_collectionid_shares_id_get(self):
        """
        Test case for collections_collectionid_shares_id_get

        Get details about a share resource
        """
        pass

    def test_collections_count_get(self):
        """
        Test case for collections_count_get

        Get a count of collections.
        """
        pass

    def test_collections_get(self):
        """
        Test case for collections_get

        Get a list of collections.
        """
        pass

    def test_collections_id_delete(self):
        """
        Test case for collections_id_delete

        Delete an existing Collection.
        """
        pass

    def test_collections_id_get(self):
        """
        Test case for collections_id_get

        Get details about a collection.
        """
        pass

    def test_collections_id_put(self):
        """
        Test case for collections_id_put

        Create or update a collection
        """
        pass

    def test_collections_post(self):
        """
        Test case for collections_post

        Create a new collection.
        """
        pass

    def test_groups_get(self):
        """
        Test case for groups_get

        Get a collection of groups.
        """
        pass

    def test_groups_id_delete(self):
        """
        Test case for groups_id_delete

        Delete an existing group.
        """
        pass

    def test_groups_id_get(self):
        """
        Test case for groups_id_get

        Get details about a group.
        """
        pass

    def test_groups_id_put(self):
        """
        Test case for groups_id_put

        Create a new or update an existing group.
        """
        pass

    def test_invitations_id_accept_post(self):
        """
        Test case for invitations_id_accept_post

        Accepts an invitation
        """
        pass

    def test_invitations_id_get(self):
        """
        Test case for invitations_id_get

        Get details about an invitation
        """
        pass

    def test_invitations_post(self):
        """
        Test case for invitations_post

        Send a new invitation
        """
        pass

    def test_locations_count_get(self):
        """
        Test case for locations_count_get

        Get a count of locations.
        """
        pass

    def test_locations_get(self):
        """
        Test case for locations_get

        Get a collection of locations.
        """
        pass

    def test_locations_id_delete(self):
        """
        Test case for locations_id_delete

        Delete an existing location.
        """
        pass

    def test_locations_id_get(self):
        """
        Test case for locations_id_get

        Get details about a location.
        """
        pass

    def test_locations_id_put(self):
        """
        Test case for locations_id_put

        Create a new or update an existing Location
        """
        pass

    def test_observations_delete(self):
        """
        Test case for observations_delete

        Delete observations from a stream
        """
        pass

    def test_observations_get(self):
        """
        Test case for observations_get

        Get a collection of observations.
        """
        pass

    def test_observations_post(self):
        """
        Test case for observations_post

        Upload observations for a stream
        """
        pass

    def test_organisations_get(self):
        """
        Test case for organisations_get

        Get a collection of organisations.
        """
        pass

    def test_organisations_organisationid_get(self):
        """
        Test case for organisations_organisationid_get

        Get details about an organisation.
        """
        pass

    def test_organisations_organisationid_put(self):
        """
        Test case for organisations_organisationid_put

        Update or create a new organisation.
        """
        pass

    def test_platforms_get(self):
        """
        Test case for platforms_get

        Get a collection of platforms.
        """
        pass

    def test_platforms_id_delete(self):
        """
        Test case for platforms_id_delete

        Delete an existing platform.
        """
        pass

    def test_platforms_id_get(self):
        """
        Test case for platforms_id_get

        Get details about a platform.
        """
        pass

    def test_platforms_id_put(self):
        """
        Test case for platforms_id_put

        Create a new or update an existing platform.
        """
        pass

    def test_procedures_get(self):
        """
        Test case for procedures_get

        Get a collection of sensing procedures.
        """
        pass

    def test_procedures_id_delete(self):
        """
        Test case for procedures_id_delete

        Delete an existing sensing procedure.
        """
        pass

    def test_procedures_id_get(self):
        """
        Test case for procedures_id_get

        Get details about a sensing procedures.
        """
        pass

    def test_procedures_id_put(self):
        """
        Test case for procedures_id_put

        Create a new or update an existing sensing procedure.
        """
        pass

    def test_roles_get(self):
        """
        Test case for roles_get

        Get a collection of roles.
        """
        pass

    def test_roles_roleid_delete(self):
        """
        Test case for roles_roleid_delete

        Delete an existing role.
        """
        pass

    def test_roles_roleid_get(self):
        """
        Test case for roles_roleid_get

        Get details about a specific role.
        """
        pass

    def test_roles_roleid_put(self):
        """
        Test case for roles_roleid_put

        Update or create a role.
        """
        pass

    def test_root_get(self):
        """
        Test case for root_get

        Sensor Data API Root
        """
        pass

    def test_shares_count_get(self):
        """
        Test case for shares_count_get

        Get a count of current shares.
        """
        pass

    def test_shares_get(self):
        """
        Test case for shares_get

        Get a list of current shares.
        """
        pass

    def test_shares_id_delete(self):
        """
        Test case for shares_id_delete

        Delete an existing Share.
        """
        pass

    def test_shares_id_get(self):
        """
        Test case for shares_id_get

        Get details about a share.
        """
        pass

    def test_shares_id_put(self):
        """
        Test case for shares_id_put

        Update an existing Share.
        """
        pass

    def test_shares_post(self):
        """
        Test case for shares_post

        Create a new share.
        """
        pass

    def test_streams_count_get(self):
        """
        Test case for streams_count_get

        Count a collection of streams.
        """
        pass

    def test_streams_get(self):
        """
        Test case for streams_get

        Get a collection of streams.
        """
        pass

    def test_streams_id_delete(self):
        """
        Test case for streams_id_delete

        Delete an existing stream.
        """
        pass

    def test_streams_id_get(self):
        """
        Test case for streams_id_get

        Get details about a stream.
        """
        pass

    def test_streams_id_put(self):
        """
        Test case for streams_id_put

        Create a new or update an existing Stream.
        """
        pass

    def test_users_get(self):
        """
        Test case for users_get

        Get a collection of users.
        """
        pass

    def test_users_userid_get(self):
        """
        Test case for users_userid_get

        Get details about a user.
        """
        pass

    def test_users_userid_put(self):
        """
        Test case for users_userid_put

        Update or create a user.
        """
        pass

    def test_vocabulary_get(self):
        """
        Test case for vocabulary_get

        Search for vocabulary terms.
        """
        pass

    def test_vocabulary_proxy_get(self):
        """
        Test case for vocabulary_proxy_get

        Resolve a specific vocabulary term
        """
        pass


if __name__ == '__main__':
    unittest.main()
