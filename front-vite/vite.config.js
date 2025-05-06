import { fileURLToPath, URL } from "node:url";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import tailwindcss from "tailwindcss";
import autoprefixer from "autoprefixer";
// elementPlus按需导入
import AutoImport from "unplugin-auto-import/vite";
import Components from "unplugin-vue-components/vite";
import { ElementPlusResolver } from "unplugin-vue-components/resolvers";

export default defineConfig({
  plugins: [
    vue(),
    AutoImport({
      resolvers: [ElementPlusResolver()],
    }),
    Components({
      resolvers: [
        // 配置elementPlus采用sass样式配色系统
        ElementPlusResolver({ importStyle: "sass" }),
      ],
    }),
  ],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
  build: {
    // 添加base配置，指定静态资源的基础路径
    assetsDir: '',
    // 设置生成的静态资源的存放路径前缀
    outDir: '../back-django/static',
    // 将 index.html 输出到 template 目录
    rollupOptions: {
      input: {
        main: fileURLToPath(new URL("./index.html", import.meta.url)),
      },
      output: {
        // JS入口文件
        entryFileNames: "assets/js/[name].[hash].js",
        // 代码分割后的chunk文件
        chunkFileNames: "assets/js/[name].[hash].js",
        // CSS、图片等资源文件
        assetFileNames: (assetInfo) => {
          const info = assetInfo.name.split('.')
          let extType = info[info.length - 1]
          if (/\.(png|jpe?g|gif|svg|webp|ico)$/.test(assetInfo.name)) {
            extType = 'imgs'
          } else if (/\.css$/.test(assetInfo.name)) {
            extType = 'css'
          } else if (/\.(woff2?|eot|ttf|otf)$/.test(assetInfo.name)) {
            extType = 'fonts'
          }
          return `assets/${extType}/[name].[hash][extname]`
        },
        // 将 index.html 输出到上级目录的 template 文件夹
        dir: '../back-django/static',
        paths: {
          'index.html': '../template/index.html'
        },
        manualChunks: (id) => {
          if (id.includes('node_modules')) {
            // UI框架相关
            if (id.includes('element-plus') || id.includes('@element-plus')) {
              // 将 element-plus 的 icons 单独打包，因为可能不是所有页面都需要
              if (id.includes('@element-plus/icons')) {
                return 'vendor-icons'
              }
              return 'vendor-element-plus'
            }
            // 按需加载的大型库
            if (id.includes('echarts')) {
              return 'vendor-echarts'
            }
            if (id.includes('xlsx')) {
              return 'vendor-xlsx'
            }
            // 核心框架保持不变
            if (id.includes('@vue') || id.includes('vue') || id.includes('pinia')) {
              return 'vendor-core'
            }
            // 其他小型依赖合并
            return 'vendors'
          }
          // 业务代码保持当前的分包策略
          return id.includes('/views/') ? 'views' : 'common'
        }
      }
    }
  },
  css: {
    preprocessorOptions: {
      scss: {
        silenceDeprecations: ["legacy-js-api"],
        additionalData: `
          @use "@/styles/element/index.scss" as *;
          @use "@/styles/var.scss" as *;
        `,
      },
    },
    postcss: {
      plugins: [tailwindcss, autoprefixer],
    },
  },
});
