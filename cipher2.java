import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.spec.InvalidKeySpecException;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;

public class HashTo6Digits {

    // 定义一个固定的盐值
    private static final byte[] SALT = "random_salt_value".getBytes(StandardCharsets.UTF_8);

    public static void main(String[] args) {
        // 获取系统当前日期并转换为 8 位数字
        int original = getCurrentDateAsOriginal();

        // 将 8 位数字加密为 6 位数字
        int encrypted = encryptTo6Digits(original);

        System.out.println("原始数字: " + original);
        System.out.println("加密结果(6位数字): " + encrypted);
    }

    public static int encryptTo6Digits(int num) {
        // 检查数字是否为 8 位
        if (num < 10000000 || num > 99999999) {
            throw new IllegalArgumentException("输入必须为 8 位数字");
        }

        try {
            // 转为字符串并计算哈希值
            String numStr = String.valueOf(num);

            // 使用 PBKDF2WithHmacSHA256 计算哈希值
            PBEKeySpec spec = new PBEKeySpec(numStr.toCharArray(), SALT, 100_000, 256);
            SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
            byte[] hashBytes = factory.generateSecret(spec).getEncoded();

            // 取前 4 个字节，转换为整数
            int hashInt = ((hashBytes[0] & 0xFF) << 24) | ((hashBytes[1] & 0xFF) << 16)
                    | ((hashBytes[2] & 0xFF) << 8) | (hashBytes[3] & 0xFF);

            // 限制结果为 6 位数字
            return Math.abs(hashInt % 1_000_000);
        } catch (NoSuchAlgorithmException | InvalidKeySpecException e) {
            throw new RuntimeException("加密错误", e);
        }
    }

    public static int getCurrentDateAsOriginal() {
        // 获取当前日期并格式化为 YYYYMMDD
        LocalDate currentDate = LocalDate.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyyMMdd");
        return Integer.parseInt(currentDate.format(formatter));
    }
}
