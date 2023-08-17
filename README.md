### Step-by-Step Guide:
1. **Fork the Repository**: Fork the main repository to your GitHub account.
2. **Clone Your Fork**: Clone the forked repository to your local machine.
3. **Create a New Branch**: Create a new branch for your changes (e.g., `feature/add-new-endpoint`).
4. **Create a YAML File**: Create a new YAML file for the endpoint you're defining.
5. **Define the Endpoint**: Define the endpoint using the OpenAPI 3.0 specification. The YAML file must contain only one endpoint, include the URL, and follow the specific requirements:
   - Endpoint URL must be included.
   - Descriptions must not exceed 150 characters.
   - Summary must not exceed 500 characters.
   - All components must be defined directly in the endpoint, not using references.
6. **Validate the YAML File**: Run a local script or use an online OpenAPI validator to ensure the YAML file meets the specifications.
7. **Commit Your Changes**: Commit your changes to your branch.
8. **Push to GitHub**: Push your branch to your fork on GitHub.
9. **Create a Pull Request**: Create a pull request from your fork to the main repository. Include a description summarizing the endpoint you're adding.
10. **Address Review Comments**: Address any comments from the maintainers and make necessary updates.
11. **Wait for Merge**: Wait for the maintainers to review and merge your pull request.

### README:

# Contributing to Our API Integrations

Thank you for considering contributing to our API integrations! Here's a detailed guide to help you add new endpoints.

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
