#!/bin/zsh

print_usage() {
    printf "Usage: -m is the only valid flag, and -m flag must have argument\n"
    printf "Example: ./gitupdate.sh -m \"fix bug\"\n" 
}

printf "-----------------\n"
printf "cleaning up\n"
printf "-----------------\n"
du -h -d 01
printf "-----------------\n"
git gc
printf "-----------------\n"
du -h -d 01
printf "-----------------\n"

# if cleanup fails due to 'failed to run repack'
# git gc --aggressive --prune=now

printf "-----------------\n"
printf "starting update\n"
printf "-----------------\n"

printf "git status\n"
git status
printf "-----------------\n"

printf "git add all\n"
git add --all
printf "-----------------\n"

printf "git commit\n"
if [ $# -eq 0 ]
then git commit -m "update"
else
    while getopts 'm:' flag; do
        case "${flag}" in
            m) git commit -m "${OPTARG}" ;;
            *) print_usage
            exit 1 ;;
        esac
    done
fi
printf "-----------------\n"

printf "git push\n"
git push
printf "-----------------\n"

printf "update complete\n"
printf "-----------------\n"

exit 0