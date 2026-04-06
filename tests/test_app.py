import pytest

def test_header_present(dash_duo):
    from app import app
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert header.text == "Daily Sales Data for Pink Morsels"

def test_graph_present(dash_duo):
    from app import app
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-line")
    assert graph is not None

def test_region_picker_present(dash_duo):
    from app import app
    dash_duo.start_server(app)

    radio = dash_duo.find_element("#region")
    assert radio is not None