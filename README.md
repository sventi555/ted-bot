# ted-bot
A bot to send daily ted talks to a slack channel.

# Docker usage
1. The environment variable `HOOK_URL` needs to be set with the slack webhook url.
2. A directory needs to be mounted to `/app/artifacts` to store a history of previous posts to the workspace.

