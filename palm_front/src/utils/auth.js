// src/utils/auth.js
export function isAuthenticated() {
    // 示例：检查 localStorage 中是否存在 token
    const token = localStorage.getItem('token');
    return !!token;
}
