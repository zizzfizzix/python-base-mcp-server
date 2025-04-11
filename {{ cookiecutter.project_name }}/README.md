# {{ cookiecutter.project_name }}

> {{ cookiecutter.project_short_description }}

## Installation

### Using uvx (recommended)

When using uvx no specific installation is needed. We will use it to directly run *{{ cookiecutter.project_slug }}* from the client app.

#### Add to Claude desktop with uvx

In your Claude config specify:

```json
"mcpServers": {
  "{{ cookiecutter.project_slug }}": {
    "command": "uvx",
    "args": [
      "--from",
      "git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}",
      "{{ cookiecutter.project_slug }}"
    ]
  }
}
```

#### Add to Zed with uvx

In your Zed settings.json add:

```json
"context_servers": [
  "{{ cookiecutter.project_slug }}": {
    "command": "uvx",
    "args": [
      "--from",
      "git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}",
      "{{ cookiecutter.project_slug }}"
    ]
  }
],
```

### Using make

Alternatively you can install `{{ cookiecutter.project_slug }}` using make:

```bash
make install
```

#### Add to Claude desktop with make

In your Claude config specify:

```json
"mcpServers": {
  "{{ cookiecutter.project_slug }}": {
    "command": "/path/to/{{ cookiecutter.project_name }}/.venv/bin/python",
    "args": ["/path/to/{{ cookiecutter.project_name }}/{{ cookiecutter.project_slug }}/main.py"]
  }
}
```

#### Add to Zed with make

In your Zed settings.json add:

```json
"context_servers": {
  "{{ cookiecutter.project_slug }}": {
    "command": "/path/to/{{ cookiecutter.project_name }}/.venv/bin/python",
    "args": ["/path/to/{{ cookiecutter.project_name }}/{{ cookiecutter.project_slug }}/main.py"]
  }
},
```

## Usage

After you've successfully added this MCP server to your assistant app follow the next steps below.

### 1. Configuration (Optional)

You can configure the server using environment variables in your client app's settings. For example:

```json
"mcpServers": {
  "{{ cookiecutter.project_slug }}": {
    "command": "uvx",
    "args": [
      "--from",
      "git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}",
      "{{ cookiecutter.project_slug }}"
    ],
    "env": {
      "EXAMPLE_VAR": "example_value"
    }
  }
}
```

## Examples

Usage examples go here.

## Development

For development, you can use the following commands:

```bash
# Install dependencies
make install

# Start the server
make start

# Run tests
make test

# Run linting
make lint

# Format code
make format
```

### Debugging

You can use the MCP inspector to debug the server.

```bash
make mcp_inspector
```

### Creating from Template

This MCP server was created from a cookiecutter template. To create a similar one, run:

```bash
uvx cookiecutter gh:zizzfizzix/python-base-mcp-server
```

## License

{{ cookiecutter.project_name }} is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.
