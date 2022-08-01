#!/bin/bash
set -eE -o functrace

failure() {
  local lineno=$1
  local msg=$2
  echo "Failed at $lineno: $msg"
}
trap 'failure ${LINENO} "$BASH_COMMAND"' ERR

set -o pipefail

WORKDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

main(){
  # shellcheck disable=SC1091
  source .activate

  pip install -r requirements.txt
  pip install -r requirements-dev.txt

  pre-commit install
}

main "$@"
