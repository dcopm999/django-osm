from django.test import TestCase
from django.test.client import Client


class URLCase(TestCase):
    databases = "__all__"
    fixtures = ["osm"]

    def setUp(self):
        self.client = Client()
        self.point = "69.279737,41.311273"

    def test_country_code(self):
        response = self.client.get("/api/country/")
        self.assertEqual(response.status_code, 200)

    def test_building_code(self):
        response = self.client.get("/api/building/")
        self.assertEqual(response.status_code, 200)

    def test_landuse_code(self):
        response = self.client.get("/api/landuse/")
        self.assertEqual(response.status_code, 200)

    def test_natural_code(self):
        response = self.client.get("/api/natural/")
        self.assertEqual(response.status_code, 200)

    def test_naturala_code(self):
        response = self.client.get("/api/naturala/")
        self.assertEqual(response.status_code, 200)

    def test_place_code(self):
        response = self.client.get("/api/place/")
        self.assertEqual(response.status_code, 200)

    def test_placea_code(self):
        response = self.client.get("/api/placea/")
        self.assertEqual(response.status_code, 200)

    def test_pofw_code(self):
        response = self.client.get("/api/pofw/")
        self.assertEqual(response.status_code, 200)

    def test_pofwa_code(self):
        response = self.client.get("/api/pofwa/")
        self.assertEqual(response.status_code, 200)

    def test_pois_code(self):
        response = self.client.get("/api/pois/")
        self.assertEqual(response.status_code, 200)

    def test_poisa_code(self):
        response = self.client.get("/api/poisa/")
        self.assertEqual(response.status_code, 200)

    def test_railway_code(self):
        response = self.client.get("/api/railway/")
        self.assertEqual(response.status_code, 200)

    def test_road_code(self):
        response = self.client.get("/api/road/")
        self.assertEqual(response.status_code, 200)

    def test_traffic_code(self):
        response = self.client.get("/api/traffic/")
        self.assertEqual(response.status_code, 200)

    def test_traffica_code(self):
        response = self.client.get("/api/traffica/")
        self.assertEqual(response.status_code, 200)

    def test_transport_code(self):
        response = self.client.get("/api/transport/")
        self.assertEqual(response.status_code, 200)

    def test_transporta_code(self):
        response = self.client.get("/api/transporta/")
        self.assertEqual(response.status_code, 200)

    def test_water_code(self):
        response = self.client.get("/api/water/")
        self.assertEqual(response.status_code, 200)

    def test_waterway_code(self):
        response = self.client.get("/api/waterway/")
        self.assertEqual(response.status_code, 200)

    def test_filters_PointDistFilter_match(self):
        response = self.client.get(
            "/api/country/", {"dist": "100000", "point": self.point}
        )
        self.assertEqual(response.data["count"], 1)

    def test_filters_PointIntersectsFilter_match(self):
        response = self.client.get("/api/country/", {"intersects": self.point})
        self.assertEqual(response.data["count"], 1)

    def test_filters_PointContainsFilter_match(self):
        response = self.client.get("/api/country/", {"contains": self.point})
        self.assertEqual(response.data["count"], 1)
