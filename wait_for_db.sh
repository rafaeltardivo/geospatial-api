set -e
until timeout 1 bash -c "cat < /dev/null > /dev/tcp/$1/$2"; do
  >&2 echo "db not ready"
  sleep 1
done

echo "db ready"