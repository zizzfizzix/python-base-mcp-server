# {{ cookiecutter.project_name }}

> {{ cookiecutter.project_short_description }}

## Installation

### Using uv (recommended)

When using [`uv`](https://docs.astral.sh/uv/) no specific installation is needed. We will use [`uvx`](https://docs.astral.sh/uv/guides/tools/) to directly run *{{ cookiecutter.project_slug }}*.

### Using make

Alternatively you can install `{{ cookiecutter.project_slug }}` using make:
```bash
make install
```

After installation, you can run it using:
```bash
make start
```

## Configuration

### Configure for Claude.app

Add to your Claude settings:

Using uvx
```json
"mcpServers": {
  "{{ cookiecutter.project_slug }}": {
    "command": "uvx",
    "args": ["{{ cookiecutter.project_slug }}"]
  }
}
```

Using docker
```json
"mcpServers": {
  "{{ cookiecutter.project_slug }}": {
    "command": "docker",
    "args": ["run", "-i", "--rm", "mcp/{{ cookiecutter.project_slug }}"]
  }
}
```

### Configure for Zed

Add to your Zed settings.json:

Using uvx
```json
"context_servers": [
  "{{ cookiecutter.project_slug }}": {
    "command": "uvx",
    "args": ["{{ cookiecutter.project_slug }}"]
  }
],
```

Using make installation
```json
"context_servers": {
  "{{ cookiecutter.project_slug }}": {
    "command": "make",
    "args": ["start"]
  }
},
```

## Debugging

You can use the MCP inspector to debug the server. For uvx installations:
```bash
make mcp_inspector
```

## Development

For development, you can use the following commands:

```bash
# Install dependencies
make install

# Run tests
make test

# Run linting
make lint

# Format code
make format
```

## License

{{ cookiecutter.project_name }} is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.