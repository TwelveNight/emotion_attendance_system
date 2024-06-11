import { defineConfig, splitVendorChunkPlugin } from 'vite'

export default defineConfig({
  css: {
    modules: {
      localsConvention: 'camelCaseOnly',
      original: 'camelCase',
    },
  }
})