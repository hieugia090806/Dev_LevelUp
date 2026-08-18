# 1. GLOBAL SCOPE (Toàn cục): Nằm ngoài cùng, ai cũng đọc được
x = "Toàn cục (Global)"

def ham_cha():
    # 2. ENCLOSING SCOPE (Phụ cận): Nằm trong hàm cha
    y = "Phụ cận (Enclosing)"
    
    def ham_con():
        # 3. LOCAL SCOPE (Cục bộ): Nằm trong hàm con
        z = "Cục bộ (Local)"
        
        # Hàm con có thể nhìn thấy và in ra cả 3 biến từ trong ra ngoài
        print("Trong hàm con:")
        print(f"- z là: {z}")
        print(f"- y là: {y}")
        print(f"- x là: {x}")

    ham_con()
    
    # Thử nghiệm lỗi (Bỏ comment dòng dưới sẽ bị lỗi ngay)
    # print(z) # LỖI! Hàm cha không thể nhìn thấy biến Local 'z' của hàm con

# Chạy thử hàm
ham_cha()
