from mcp.server.fastmcp import FastMCP
from {{ cookiecutter.project_slug }}.services.weather import WeatherRepository, WeatherService
from {{ cookiecutter.project_slug }}.tools.weather import add_weather_tools

mcp = FastMCP("{{ cookiecutter.project_name }}")

weather_repository = WeatherRepository("weather-app/1.0")
weather_service = WeatherService("https://api.weather.gov", weather_repository)
add_weather_tools(mcp, weather_service)

if __name__ == "__main__":
    mcp.run(transport="stdio")
