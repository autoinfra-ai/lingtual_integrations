import yaml
from openapi_spec_validator import validate_spec

def validate_descriptions(data, max_description_length, max_summary_length):
    for path, methods in data['paths'].items():
        for method, details in methods.items():
            # Validate endpoint summary
            summary = details.get('summary', '')
            if len(summary) > max_summary_length:
                raise ValueError(f"Summary too long for {method} {path}")

            # Validate parameter descriptions
            for param in details.get('parameters', []):
                description = param.get('description', '')
                if len(description) > max_description_length:
                    raise ValueError(f"Description too long for parameter {param['name']} in {method} {path}")

            # Validate response descriptions
            for response in details.get('responses', {}).values():
                description = response.get('description', '')
                if len(description) > max_description_length:
                    raise ValueError(f"Description too long for response in {method} {path}")

def validate_single_endpoint(data):
    if len(data['paths']) != 1:
        raise ValueError("Only one endpoint is allowed per YAML file")

def validate_no_component_refs(data):
    for path, methods in data['paths'].items():
        for method, details in methods.items():
            # Check if any components are referenced
            if '$ref' in str(details):
                raise ValueError(f"Components references are not allowed in {method} {path}")

def validate_endpoint_url(data):
    if 'servers' not in data or not data['servers']:
        raise ValueError("URL for the endpoint must be defined")

def main(yaml_file):
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    # Validate OpenAPI schema
    validate_spec(data)

    # Validate custom requirements
    max_description_length = 150
    max_summary_length = 500
    validate_descriptions(data, max_description_length, max_summary_length)
    validate_single_endpoint(data)
    validate_no_component_refs(data)
    validate_endpoint_url(data)

    print("OpenAPI YAML is valid!")

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python validate_openapi.py <path_to_yaml>")
        sys.exit(1)

    yaml_file = sys.argv[1]
    main(yaml_file)
