# DLove Photobouquet - Bản Crawl Hoàn Chỉnh

Trang web thiệp chúc mừng 3D tương tác được crawl từ:
`https://i.dlove.vn/index.html?fc8e1763db7249b6`

---

## 1. Cấu trúc thư mục

- [`index.html`](./index.html): File HTML chính của web thiệp.
- [`serve.py`](./serve.py): Script khởi chạy local web server (tự động nhận cổng trống, cấu hình đúng MIME types cho file 3D `.obj`, âm thanh `.mp3`, ảnh `.webp`, và CORS).
- [`card_data.json`](./card_data.json): Dữ liệu cấu hình gốc từ API (`https://apiv2.deargift.online/api/v2/access/photobouquet/fc8e1763db7249b6`).
- [`card_data_offline.json`](./card_data_offline.json): Dữ liệu cấu hình đã được bản địa hoá 100%, trỏ toàn bộ ảnh và nhạc về thư mục offline [`user_media/`](./user_media/).
- [`user_media/`](./user_media/): Chứa toàn bộ 17 file media của thiệp (6 ảnh bó hoa, 10 ảnh bay, 1 ảnh trong bức thư, 1 bài hát nền).
- [`assets/`](./assets/): Chứa các module JavaScript (Three.js, React Three Fiber, hiệu ứng StarField...), CSS, ảnh trang trí hoa, nơ, phong bì thư.
- [`models/heart.obj`](./models/heart.obj): Mô hình 3D trái tim dùng trong hoạt cảnh Three.js.
- [`font/`](./font/): Font chữ hiển thị (Mali, DancingScript, Allura).

---

## 2. Thông tin thiệp đã crawl (`fc8e1763db7249b6`)

- **Loại thiệp:** Photobouquet (Bó hoa hình ảnh 3D)
- **Tiêu đề phong bì:**
  - Dòng trên: *Dành tặng em*
  - Tiêu đề chính: *20/10*
  - Dòng dưới: *Một chút yêu thương*
- **Nội dung thư:**
  > "Gửi cô gái bé nhỏ của anh
  > 
  > Anh chúc em ngày 20/10 lúc nào cũng xinh đẹp, may mắn, nhiều sức khỏe và lúc nào cũng vui vẻ. Anh mong rằng em sẽ đồng hành cùng anh trên chặng đường phía trước.
  > Cảm ơn em vì tất cả. 🫶
  > Anh yêu em bé của anh."
- **Các lời chúc bay:**
  - *Chúc em luôn vui vẻ và hạnh phúc*
  - *Chúc em luôn xinh đẹp*
  - *Chúc em luôn yêu đời*
  - *Chúc mừng ngày phụ nữ việt nam*
  - *20/10*
  - *yêu em*
  - *chúc em thật nhiều may mắn*
  - *mãi yêu em*
  - *Mong mọi điều dịu dàng sẽ đến với em*
- **Nhạc nền:** Đã tải về tại [`user_media/audio-mv9ff9kg-7edf2bd9.mp3`](./user_media/audio-mv9ff9kg-7edf2bd9.mp3)

---

## 3. Cách mở và chạy cục bộ (Offline)

Chỉ cần chạy lệnh sau từ terminal:

```bash
cd /home/dinhquang/Workspaces/youtube-control-design/dlove-crawled
python3 serve.py
```

Sau đó mở trình duyệt và truy cập:
`http://localhost:8000` (hoặc cổng mà terminal thông báo).

---

## 4. Tuỳ biến dữ liệu

Bạn có thể chỉnh sửa nội dung bức thư, lời chúc, danh sách ảnh hoặc thay nhạc nền bất kỳ lúc nào bằng cách sửa file [`card_data_offline.json`](./card_data_offline.json).
