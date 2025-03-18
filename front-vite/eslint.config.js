import globals from "globals";
import pluginJs from "@eslint/js";
import tseslint from "typescript-eslint";
import pluginVue from "eslint-plugin-vue";


/** @type {import('eslint').Linter.Config[]} */
export default [{
    files: ["**/*.{js,mjs,cjs,ts,vue}"],
    ignores: ["src/scripts/**"]
  },
  {
    languageOptions: {
      globals: globals.browser
    }
  },
  pluginJs.configs.recommended,
  ...tseslint.configs.recommended,
  {
    rules: {
      '@typescript-eslint/no-explicit-any': 'off',
      '@typescript-eslint/no-unused-vars': 'off',
      // '@typescript-eslint/no-non-null-assertion': 'off',
      'no-prototype-builtins': 'off'
    }
  },
  ...pluginVue.configs["flat/essential"],
  {
    files: ["**/*.vue"],
    languageOptions: {
      parserOptions: {
        parser: tseslint.parser
      }
    },
    rules: {
      'vue/no-multiple-template-root': 'off',
      'vue/valid-template-root': 'off',
      'vue/multi-word-component-names': ['error', {
        ignores: ['index', 'Header', 'Footer', 'Main', 'Layout', 'View', 'Content', 'Percent', 'Home', 'About', 'Login']
      }]
    }
  },
];