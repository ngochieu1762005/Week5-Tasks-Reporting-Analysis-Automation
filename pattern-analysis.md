# Pattern Analysis

## Mục tiêu

Mục tiêu của phần này là nhìn vào dữ liệu ticket thật từ Odoo để tìm ra các nhóm vấn đề lặp lại. Không chỉ nhìn từng ticket riêng lẻ, mà nhóm ticket theo tag, nội dung subject và mức độ ảnh hưởng tới vận hành.

Dataset dùng cho phần này gồm 131 ticket từ `sample.xlsx`.

## 1. Pattern tổng quan

Từ dữ liệu export, các nhóm issue nổi bật nhất là:

| Rank | Pattern | Evidence từ dữ liệu | Nhận xét |
|---:|---|---|---|
| 1 | CRM issues | 25 ticket có tag CRM | Nhóm lớn nhất, liên quan lead, enrollment, payment, dropout, gọi điện |
| 2 | LMS issues | 20 ticket có tag LMS | Liên quan lớp học, học viên, enrollment, Denise/Ecount, tài khoản |
| 3 | TMS issues | 9 ticket có tag TMS | Liên quan truy cập, công, dữ liệu TMS |
| 4 | Account / mail / access | 5 ticket mail + 3 ticket tài khoản Denise + các ticket cấp lại tài khoản | Phù hợp để chuẩn hóa checklist và automation một phần |
| 5 | Bug / system error | 5 ticket có tag Bug, nhiều subject có từ khóa lỗi/fix | Cần escalation hoặc root cause analysis kỹ hơn |
| 6 | Payment / QR / confirm | Có ticket QR, payment, confirm giao dịch | Cần quy trình kiểm tra rõ giữa CRM/kế toán/hệ thống |

## 2. Pattern lặp lại theo subject

Một số subject xuất hiện lặp lại hoặc rất giống nhau:

| Pattern | Số lần thấy trong export | Ví dụ |
|---|---:|---|
| Tech test | 3 | Tech test, Fwd: Tech test |
| Ecount và Denise không thống nhất số lượng đổi quà | 2 | Số lượng giữa 2 hệ thống ECOUNT và DENISE không thống nhất |
| Sửa tên trong enrollment của học viên | 2 | Nhờ team tech sửa lại tên đúng trong enrollment |
| Không tạo được phiếu dropout | 2 | BU PXL I không tạo được phiếu dropout |
| Lỗi enroll / không thể enroll học viên | 2+ | LỖI ENROLL, KHÔNG THỂ ENROLL HỌC VIÊN |
| CRM không bấm gọi được | 2 | CRM không bấm gọi được |
| Cấp mail Outlook | 2 | Cấp mail Outlook để làm việc nội bộ |

Các pattern này cho thấy nhiều ticket không phải sự cố hoàn toàn mới, mà là các dạng request/lỗi có thể tái diễn.

## 3. Impact analysis

### Theo priority

| Priority | Count | Ý nghĩa |
|---|---:|---|
| Urgent | 40 | Cần phản hồi nhanh, dễ ảnh hưởng trực tiếp tới vận hành |
| High priority | 42 | Cần ưu tiên theo dõi và xử lý |
| Medium priority | 9 | Ít hơn đáng kể so với các nhóm khác |
| Low priority | 40 | Có thể xử lý theo queue bình thường |

Điểm đáng chú ý là số lượng ticket `Urgent` và `High priority` rất cao. Nếu không có quy trình phân loại và escalation tốt, team support sẽ dễ bị quá tải.

### Theo hệ thống

CRM và LMS là hai hệ thống cần ưu tiên nhất vì số lượng ticket cao nhất. TMS tuy ít hơn nhưng các ticket TMS thường liên quan trực tiếp tới việc truy cập hệ thống hoặc dữ liệu công, nên vẫn cần checklist riêng.

## 4. Root cause ban đầu

| Pattern | Root cause có thể | Hướng xử lý đề xuất |
|---|---|---|
| CRM / lead / enrollment | Dữ liệu lead/enrollment sai, thao tác nghiệp vụ phức tạp, thiếu validation | Chuẩn hóa checklist, bổ sung KB, xem xét automation cho các thao tác lặp lại |
| LMS / học viên / lớp học | Đồng bộ dữ liệu giữa LMS, Denise, Ecount hoặc lỗi enrollment | Monitoring đồng bộ dữ liệu, checklist xử lý LMS |
| Account / mail / access | User thiếu quyền, tài khoản bị khóa, cần cấp lại hoặc kiểm tra trạng thái | Phù hợp automation một phần: check trạng thái user rồi xử lý theo rule |
| Bug / system error | Lỗi hệ thống hoặc logic nghiệp vụ | Cần escalation dev/infra, không nên auto-fix nếu chưa rõ nguyên nhân |
| Payment / QR / confirm | Lỗi luồng thanh toán/confirm, dữ liệu giữa kế toán và CRM | Cần quy trình kiểm tra liên phòng ban |

## 5. Chọn issue phù hợp để automation

Dựa trên dữ liệu thật, chọn hướng **Login / Account Access Automation** vì nhóm access/account xuất hiện nhiều dạng khác nhau:

- Cấp lại tài khoản Ecount
- Cấp mail Outlook
- Tài khoản Denise học viên không đăng nhập được
- Không truy cập được TMS
- Các request liên quan quyền truy cập hoặc tài khoản

Nhóm này phù hợp automation hơn các bug phức tạp vì có thể xử lý theo rule an toàn:

1. Đọc ticket và nhận diện account/login/access issue.
2. Lấy email hoặc thông tin requester.
3. Check HR/user status.
4. Nếu user active thì xử lý bước an toàn như reactivate/unlock theo policy.
5. Nếu terminated/unknown/suspended thì chuyển manual review.

## Kết luận

Dữ liệu thật cho thấy các vấn đề nổi bật không chỉ nằm ở LMS mà còn có CRM, TMS, mail/account và các lỗi đồng bộ dữ liệu. Trong đó, nhóm login/account/access là nhóm phù hợp để automation theo Operating Engineer approach vì có thể đặt boundary rõ ràng và giảm thao tác thủ công mà vẫn đảm bảo an toàn.
