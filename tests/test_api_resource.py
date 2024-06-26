from iots.api import API


def test_build_url():
    """
    Builds the full URL of a chained call successfully.
    """
    api = API(host="test-api.swx.altairone.com")
    prop = api.spaces("space01").categories("cat01").things("thing01").properties("temperature")

    assert prop._build_url() == "https://test-api.swx.altairone.com" \
                                "/spaces/space01/categories/cat01/things/thing01/properties/temperature"


def test_build_path():
    """
    Builds the URL path of a chained call successfully.
    """
    api = API(host="test-api.swx.altairone.com")

    cat = api.spaces("space01").categories("cat01")
    thing1 = cat.things("thing01")
    thing2 = cat.things("thing02")
    prop_thing1 = thing1.properties("temperature")
    prop_thing2 = thing2.properties("humidity")

    assert cat._build_path() == "/spaces/space01/categories/cat01"
    assert thing1._build_path() == "/spaces/space01/categories/cat01/things/thing01"
    assert thing2._build_path() == "/spaces/space01/categories/cat01/things/thing02"
    assert prop_thing1._build_path() == "/spaces/space01/categories/cat01/things/thing01/properties/temperature"
    assert prop_thing2._build_path() == "/spaces/space01/categories/cat01/things/thing02/properties/humidity"
    assert api.spaces("space01").things("thing01")._build_path() == "/spaces/space01/things/thing01"
    assert api.spaces("space01").categories()._build_path() == "/spaces/space01/categories"
    assert api.spaces("space01").things()._build_path() == "/spaces/space01/things"
    assert api.spaces("space01")._build_path() == "/spaces/space01"
    assert thing1.properties()._build_path() == "/spaces/space01/categories/cat01/things/thing01/properties"
