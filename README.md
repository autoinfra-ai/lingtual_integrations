
# Contributing to Our API Integrations

Thank you for considering contributing to our API integrations! Here's a detailed guide to help you submit new endpoints for us to integrate!

## Quick Guidelines
- Only one endpoint per YAML file.
- A Pull Request (PR) can contain more than one YAML file if you're defining multiple endpoints.
- Follow the OpenAPI 3.0 specification.
- Make sure descriptions are no longer than 150 characters, and the endpoint summary is under 500 characters.
- No component references are allowed; include all components directly in the endpoint definition.

## Steps to Contribute
1. **Fork & Clone**: Start by forking this repository, and then clone your fork locally.
2. **Create a new yaml**: create a new yaml file in integrations/
3. **Define Your Endpoint**: Follow the guidelines above to define your endpoint in a new YAML file.
4. **Validate**: Ensure your YAML file meets our specifications. You can run `validation_openapi.py` locally to validate your file.
5. **Commit & Push**: Commit your changes and push them to your GitHub fork.
6. **Submit a Pull Request**: Create a pull request from your branch to the main repository, and describe your changes.
7. **Collaborate**: Be ready to discuss your changes and make updates as necessary.

## Need Help?
Refer to the [OpenAPI documentation](https://swagger.io/docs/specification/about/) for more information about defining your endpoint. If you have any questions, don't hesitate to reach out to the maintainers.

## Thank You!
Your contributions make our platform even better. Thank you for collaborating with us!
