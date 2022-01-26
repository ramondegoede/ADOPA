AZP_AGENT_PACKAGES=$(curl -LsS \
    -u user:$(cat "$PAT") \
    -H 'Accept:application/json;' \
    "$ORG_URL/_apis/distributedtask/packages/agent?platform=$TARGETARCH&top=1")

AZP_AGENT_PACKAGE_LATEST_URL=$(echo "$AZP_AGENT_PACKAGES" | jq -r '.value[0].downloadUrl')

if [ -z "$AZP_AGENT_PACKAGE_LATEST_URL" -o "$AZP_AGENT_PACKAGE_LATEST_URL" == "null" ]; then
    echo 1>&2 "error: could not determine a matching Azure Pipelines agent"
    echo 1>&2 "check that account '$AZP_URL' is correct and the token is valid for that account"
    exit 1
fi

print_header "2. Downloading and extracting Azure Pipelines agent..."

curl -LsS $AZP_AGENT_PACKAGE_LATEST_URL | tar -xz & wait $!