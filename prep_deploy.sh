source venv/bin/activate

doit js:build

mkdir -p frontend/build/root
for file in $(ls frontend/build | grep -E -v '^(index\.html|static|root)$'); do
    mv "frontend/build/$file" frontend/build/root;
done

doit collect
