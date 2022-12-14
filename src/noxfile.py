import nox


@nox.session(python=['3.8.10'])
def lint(session):
    session.install('flake8')
    session.run(
        'flake8',
        '--ignore=F401,F811,W503',
        '.')
