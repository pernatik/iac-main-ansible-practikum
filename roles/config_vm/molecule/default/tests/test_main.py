import pytest


@pytest.mark.parametrize("name,version", [
    ("nginx", "1.18"),
    ("openjdk-16-jdk", "16"),
    ("nodejs", "16")
])
def test_packages(host, name, version):
    package = host.package(name)
    assert package.is_installed
    assert package.version.startswith(version)


def test_users_added(host):
    app_variables = host.ansible.get_variables().get('app')
    for _, value in app_variables.items():
        assert host.user(value.get('user')).exists


def test_directory_maked(host):
    directory = host.file("/var/www-data")
    assert directory.is_directory
    assert directory.user == "www-data"
    assert directory.group == "www-data"
    assert directory.mode == 0o755


def test_backend_request(host):
    backend_request_output = host.check_output(
        "curl -o /dev/null -s -w '%{http_code}\n' \
            http://localhost:8080/api/products"
    )
    assert backend_request_output == "200"


def test_nginx_proxy_pass(host):
    nginx_request_output = host.check_output(
        "curl -o /dev/null -s -w '%{http_code}\n' \
            http://localhost/api/products"
    )
    assert nginx_request_output == "200"
