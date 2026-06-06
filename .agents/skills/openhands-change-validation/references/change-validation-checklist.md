# OpenHands Change Validation Checklist

## Classify the change

- Backend Python
- Frontend
- VSCode extension
- Enterprise
- Docs-only
- Mixed

## Baseline

- Attempt `make install-pre-commit-hooks`
- Record the exact failure if the environment cannot run it

## Validation by area

### Backend Python

- Run the most relevant targeted `pytest`
- Run `pre-commit run --config ./dev_config/python/.pre-commit-config.yaml`

### Frontend

- Run `cd frontend && npm run lint:fix && npm run build`
- Run a focused frontend test if behavior changed and one exists

### VSCode extension

- Run `cd openhands/app_server/integrations/vscode && npm run lint:fix && npm run compile`

### Enterprise

- Run enterprise-targeted tests or enterprise pre-commit as appropriate

### Docs-only

- Verify factual claims
- Check paths, commands, and links

## Finish

- Rerun checks after autofixes
- Report passed, failed, and not run separately
- State clearly whether the change is ready for push
