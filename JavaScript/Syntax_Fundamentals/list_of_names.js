function solve(firstArray) {
    return [...firstArray]
        .sort((a, b) => a.localeCompare(b))
        .map((name, index) => `${index + 1}.${name}`)
        .join('\n');
}

