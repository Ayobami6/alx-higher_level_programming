module.exports = {
    env: {
        browser: true,
        es2021: true,
    },
    extends: 'airbnb-base',
    overrides: [],
    parserOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module',
    },
    rules: {
        'no-console': 0,
        'no-restricted-globals': 0,
        'no-plusplus': 0,
        'space-before-function-paren': 0,
        'no-unused-expressions': 0,
        'func-names': 0,
    },
};
