from marshmallow import Schema, fields


class TaskSchema(Schema):

    config_id = fields.String()
    id = fields.String()
    parent_id = fields.String()
    input_ids = fields.List(fields.String)
    function_name = fields.String()
    function_module = fields.String()
    output_ids = fields.List(fields.String)
