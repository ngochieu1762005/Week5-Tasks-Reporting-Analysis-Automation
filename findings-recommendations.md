# Findings & Recommendations

## 1. Tóm tắt ngắn

Sau khi dùng dữ liệu thật từ `sample.xlsx`, em thấy bức tranh khác rõ so với bản demo 6 ticket ban đầu. Dataset có 131 ticket, trong đó CRM và LMS là hai nhóm xuất hiện nhiều nhất. Ngoài ra còn có các nhóm TMS, mail/account, bug, payment/QR và các vấn đề đồng bộ dữ liệu giữa hệ thống.

## 2. Findings chính

### Finding 1: CRM và LMS là hai nhóm ticket lớn nhất

| Nhóm | Số lượng ticket |
|---|---:|
| CRM | 25 |
| LMS | 20 |
| TMS | 9 |

CRM và LMS nên được ưu tiên theo dõi vì đây là hai nguồn phát sinh ticket lớn nhất trong export.

### Finding 2: Urgent và High priority chiếm tỷ lệ cao

| Priority | Số lượng |
|---|---:|
| Urgent | 40 |
| High priority | 42 |
| Medium priority | 9 |
| Low priority | 40 |

Có 82/131 ticket thuộc nhóm Urgent hoặc High priority. Điều này cho thấy cần có quy trình triage và escalation rõ hơn, nếu không support rất dễ bị quá tải.

### Finding 3: Một số vấn đề có tính lặp lại rõ

Một số pattern lặp lại gồm:

- Ecount và Denise không thống nhất số lượng đổi quà
- Sửa tên trong enrollment của học viên
- Không tạo được phiếu dropout
- Lỗi enroll hoặc không thể enroll học viên
- CRM không bấm gọi được
- Cấp mail Outlook / cấp lại tài khoản

Các nhóm này nên được đưa vào KB hoặc checklist để giảm thời gian xử lý.

### Finding 4: Account / login / access là nhóm phù hợp để automation

Các ticket liên quan tài khoản và quyền truy cập có thể được xử lý bằng workflow an toàn: nhận diện ticket, check trạng thái user, chỉ xử lý tự động khi đủ điều kiện, còn lại chuyển manual review.

## 3. Recommendations

### Recommendation 1: Chuẩn hóa tag khi tạo ticket

Hiện tại có khá nhiều ticket chưa có tag hệ thống rõ ràng hoặc tag còn rời rạc. Nên chuẩn hóa một số nhóm tag chính:

- CRM
- LMS
- TMS
- Mail / Account
- Payment
- Bug
- Data Sync
- Enrollment

Việc này giúp báo cáo sau này chính xác hơn và dễ tìm recurring issue hơn.

### Recommendation 2: Tạo checklist cho CRM và LMS

Vì CRM và LMS là hai nhóm lớn nhất, nên tạo checklist riêng cho các lỗi thường gặp:

- CRM: lead, enrollment, dropout, payment, call, confirm
- LMS: lớp học, học viên, bài tập, đồng bộ dữ liệu, account/login

Checklist sẽ giúp support xử lý nhanh và nhất quán hơn.

### Recommendation 3: Automation cho login/account/access issue

Nên tiếp tục triển khai automation cho nhóm login/account/access. Đây là nhóm có thể đặt rule rõ ràng và kiểm soát rủi ro.

Workflow đề xuất:

```text
Odoo Ticket
  ↓
Detect login/account/access issue
  ↓
Extract requester email
  ↓
Check HR/user status
  ↓
Active → reactivate/unlock theo policy
  ↓
Other status → manual review
  ↓
Update Odoo + send response
```

### Recommendation 4: Không auto-fix bug phức tạp

Các ticket có tag `Bug` hoặc liên quan lỗi hệ thống nên được escalation tới dev/infra sau khi support thu thập đủ context. Không nên để automation tự sửa nếu root cause chưa rõ.

### Recommendation 5: Theo dõi metric sau automation

Nếu automation được dùng, nên theo dõi các metric sau:

| Metric | Mục đích |
|---|---|
| Số ticket account/login mỗi tuần | Xem automation có giảm workload không |
| Automation success rate | Tỷ lệ xử lý tự động thành công |
| Manual review rate | Tỷ lệ cần người kiểm tra |
| Error rate | Tỷ lệ lỗi khi gọi API/HR/LMS |
| Average handling time | So sánh trước và sau automation |

## 4. Action plan

| Action | Priority | Expected outcome |
|---|---|---|
| Chuẩn hóa tag ticket | High | Report chính xác hơn |
| Viết checklist CRM/LMS | High | Giảm thời gian xử lý |
| Hoàn thiện login/account automation | High | Giảm thao tác thủ công |
| Tạo KB cho các pattern lặp lại | Medium | Support mới dễ xử lý hơn |
| Theo dõi metric automation | Medium | Đo được hiệu quả cải tiến |

## Kết luận

Dữ liệu thật cho thấy bài Week 5 nên tập trung vào CRM, LMS và nhóm account/access thay vì chỉ nhìn 6 scenario practice. Automation vẫn nên chọn login/account/access vì đây là nhóm đủ rõ để xử lý theo rule, trong khi các lỗi bug hoặc đồng bộ dữ liệu phức tạp nên được đưa vào checklist, monitoring và escalation.
