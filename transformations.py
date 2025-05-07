def apply_transformation(column_name, data, transformation_rule):
    """Applies transformations based on metadata"""
    if transformation_rule == "uppercase":
        return [str(row[0]).upper() for row in data]
    elif transformation_rule == "mask_email":
        return ["***@***.com" for row in data]
    elif transformation_rule == "convert_date":
        return [str(row[0]).split(" ")[0] for row in data]
    else:
        return [row[0] for row in data]  # No transformation

def transform_data(metadata, extracted_data):
    """Iterate over extracted data and apply transformations"""
    transformed_data = {}
    for row in metadata:
        column_name, transformation_rule = row[6], row[7]
        transformed_data[column_name] = apply_transformation(column_name, extracted_data[column_name], transformation_rule)
    
    return transformed_data
