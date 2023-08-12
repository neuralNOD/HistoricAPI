<h1 align = "center">Environment Setup</h1>

<div align = "justify">

With release of [v3.0.0](https://github.com/ZenithClown/flask-docker-template/releases/tag/v3.0.0) template, all environment variables are called directly from `$PATH` using the `os.getenv()` function, however since all project has similar *naming* constraints (when using template), end users are requested to globally change and/or fix variables. In `*.nix` based systems (considering BASH shell), the environment variable can be added and referenced through `~/.bashrc` file.

</div>
