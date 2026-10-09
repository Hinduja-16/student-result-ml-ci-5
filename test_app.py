def test_high_performance_prediction(self):
        response = self.client.post(
            "/predict",
            json={
                "attendance": 90,
                "internal_marks": 85,
                "assignment_marks": 88,
                "previous_score": 80
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["prediction"],
            "FAIL"  # <-- Make sure this line is changed in test_app.py
        )
