#! /usr/bin/env dash

# ==============================================================================
# test0.sh
# Test the take-submit command.
#
# Written by: Dylan Brotherston <d.brotherston@unsw.edu.au>
# Date: 2025-03-10
# For COMP2041/9044 Assignment 1
# ==============================================================================

# add the current directory to the PATH so scripts
# can still be executed from it after we cd

PATH="$PATH:$(pwd)"

# Create a temporary directory for the test.
test_dir="$(mktemp -d)"
cd "$test_dir" || exit 1
ref_dir="$(mktemp -d)"
cd "$ref_dir" || exit 1

# Create some files to hold output.

expected_stdout="$(mktemp)"
expected_stderr="$(mktemp)"
actual_stdout="$(mktemp)"
actual_stderr="$(mktemp)"

# Remove the temporary directory when the test is done.

trap 'rm "$expected_stdout" "$expected_stderr" "$actual_stdout" "$actual_stderr" -r "$test_dir"' INT HUP QUIT TERM EXIT

# Retrieve the provided test files.

2041 fetch take

# Create take assessment

cd "$ref_dir" || exit 1
2041 take-add lab03_scraping_courses scraping_courses.sh scraping_courses.tests scraping_courses.marking > "$expected_stdout" 2> "$expected_stderr"
ref_exit_code=$?

cd "$test_dir" || exit 1
take-add lab03_scraping_courses scraping_courses.sh scraping_courses.tests scraping_courses.marking > "$actual_stdout" 2> "$actual_stderr"
exit_code=$?

if ! diff "$expected_stdout" "$actual_stdout" >/dev/null 2>&1; then
    echo "Failed test - stdout differs"
    diff "$expected_stdout" "$actual_stdout"
    exit 1
fi

if ! diff "$expected_stderr" "$actual_stderr" >/dev/null 2>&1; then
    echo "Failed test - stderr differs"
    diff "$expected_stderr" "$actual_stderr"
    exit 1
fi

if [ "$exit_code" -ne "$ref_exit_code" ]; then
    echo "Failed test - exit code differs"
    echo "Expected: $ref_exit_code" 
    echo "Got: $exit_code"
    exit 1
fi

# All tests passed.
echo "All tests passed."