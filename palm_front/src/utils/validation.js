// src/utils/validation.js

// 验证用户名是否有效
export function validateUsername(username) {
    // 用户名长度至少为 3 个字符
    if (username.length < 3) {
        return { valid: false, message: '用户名至少需要 3 个字符' };
    }
    // 可以添加更多规则，例如只能包含字母和数字
    if (!/^[a-zA-Z0-9]+$/.test(username)) {
        return { valid: false, message: '用户名只能包含字母和数字' };
    }
    return { valid: true, message: '' };
}

// 验证密码是否有效
export function validatePassword(password) {
    // 密码长度至少为 6 个字符
    if (password.length < 6) {
        return { valid: false, message: '密码至少需要 6 个字符' };
    }
    // 可以添加更多规则，例如必须包含大写字母、小写字母、数字和特殊字符
    if (!/(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}/.test(password)) {
        return { valid: false, message: '密码必须包含大写字母、小写字母、数字和特殊字符' };
    }
    return { valid: true, message: '' };
}
