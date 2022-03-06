curl "http://localhost:8000/characters/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "character": {
      "name": "'"${NAME}"'",
      "level": "'"${LEVEL}"'",
      "exp": "'"${EXP}"'",
      "charClass": "'"${CHARCLASS}"'",
      "race": "'"${RACE}"'",
      "alignment": "'"${ALIGNMENT}"'",
      "background": "'"${BACKGROUND}"'"

    }
  }'

echo
