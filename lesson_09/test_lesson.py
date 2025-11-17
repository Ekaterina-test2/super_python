from classwbase import ForBase as tm
import config


def test_create():
    make = tm(config.db_connection_string)
    maxid = make.get_max_id()
    newid = maxid + 1
    config.old_subject["subject_id"] = newid
    make.insert_subject()
    result = make.select_subject(newid)
    rows = result.mappings().all()
    make.delete(newid)
    assert rows[0]["subject_id"] == config.old_subject["subject_id"]
    assert rows[0]["subject_title"] == config.old_subject["subject_title"]


def test_update():
    make = tm(config.db_connection_string)
    maxid = make.get_max_id()
    newid = maxid + 1
    config.old_subject["subject_id"] = newid
    make.insert_subject()
    make.update_subject(newid)
    result = make.select_subject(newid)
    make.delete(newid)
    rows = result.mappings().all()
    assert rows[0]["subject_title"] == config.update_data


def test_delete():
    make = tm(config.db_connection_string)
    maxid = make.get_max_id()
    newid = maxid + 1
    config.old_subject["subject_id"] = newid
    make.insert_subject()
    make.delete(newid)
    result = make.select_subject(newid)
    rows = result.mappings().all()
    assert len(rows) == 0
