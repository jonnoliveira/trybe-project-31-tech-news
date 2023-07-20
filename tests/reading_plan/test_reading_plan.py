from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from unittest.mock import Mock, patch

import pytest

mock_data = [
    {
        "title": "10 jogos para iniciantes aprenderem a programar!",
        "reading_time": 12,
    },
    {
        "title": "Endless OS: por que vale a pena usar esse sistema",
        "reading_time": 5,
    },
    {
        "title": "TrybeTalks – CTO do Nubank",
        "reading_time": 7,
    },
    {
        "title": "Elon Musk chegou em Marte",
        "reading_time": 17,
    },
]

expected_output = {
    "readable": [
        {
            "unfilled_time": 3,
            "chosen_news": [
                (
                    "10 jogos para iniciantes aprenderem a programar!",
                    12,
                ),
            ],
        },
        {
            "unfilled_time": 3,
            "chosen_news": [
                (
                    "Endless OS: por que vale a pena usar esse sistema",
                    5,
                ),
                (
                    "TrybeTalks – CTO do Nubank",
                    7,
                ),
            ],
        },
    ],
    "unreadable": [("Elon Musk chegou em Marte", 17)],
}


def test_reading_plan_group_news():
    mock_find_news = Mock(return_value=mock_data)

    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(0)

    with patch(
        "tech_news.analyzer.reading_plan.ReadingPlanService._db_news_proxy",
        mock_find_news,
    ):
        expected_result = ReadingPlanService.group_news_for_available_time(15)
        assert expected_result == expected_output
