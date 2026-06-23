# Odoo Reports

## Nguồn dữ liệu

Báo cáo này sử dụng dữ liệu từ file export Odoo `sample.xlsx`, gồm 131 ticket Helpdesk. Mục tiêu là biến dữ liệu ticket thô thành các báo cáo dễ đọc để phục vụ phân tích pattern và đề xuất cải tiến.

## 1. Ticket Summary Report

| Metric | Value |
|---|---:|
| Total tickets | 131 |
| New | 6 |
| First Response Sent | 17 |
| In Progress | 5 |
| Resolved | 91 |
| Cancelled | 12 |

### Nhận xét

Có 91 ticket đã được xử lý xong, chiếm phần lớn dữ liệu. Nhóm còn cần chú ý là 28 ticket đang ở `New`, `First Response Sent` hoặc `In Progress`. Nhóm này phản ánh backlog/đang xử lý tại thời điểm export.

## 2. Priority Report

| Priority | Ticket Count | Percentage |
|---|---:|---:|
| Urgent | 40 | 30.5% |
| High priority | 42 | 32.1% |
| Medium priority | 9 | 6.9% |
| Low priority | 40 | 30.5% |

### Nhận xét

Số lượng `Urgent` và `High priority` khá cao. Tổng hai nhóm này là 82 ticket, chiếm 62.6% tổng dataset. Điều này cho thấy team support cần có quy trình ưu tiên rõ ràng để tránh các ticket quan trọng bị trôi.

## 3. Category / Tag Analysis

| Tag / Category | Ticket Count |
|---|---:|
| CRM | 25 |
| LMS | 20 |
| TMS | 9 |
| User responded | 6 |
| Awaiting information | 5 |
| Các vấn đề về mail | 5 |
| Bug | 5 |
| enroll HV | 4 |
| Điểm thưởng | 3 |
| Xspace | 3 |
| Denise | 3 |
| Tài khoản Denise - HV không đăng nhập được | 3 |
| E-contract | 3 |

### Nhận xét

CRM và LMS là hai nhóm lớn nhất trong export. Đây là hai hệ thống có nhiều ticket vận hành nhất, nên cũng là hai khu vực nên ưu tiên monitoring, chuẩn hóa quy trình xử lý và tìm cơ hội automation.

## 4. System-focused Report

| Nhóm hệ thống | Số lượng ticket |
|---|---:|
| CRM | 25 |
| LMS | 20 |
| TMS | 9 |
| Xspace | 3 |
| Denise | 3 |
| E-contract | 3 |
| E-learning | 1 |
| Khác / không có tag hệ thống rõ ràng | 67 |

### Nhận xét

Không phải ticket nào cũng có tag hệ thống rõ ràng, nhưng trong các tag có thể đọc được thì CRM và LMS vẫn nổi bật nhất. Một điểm cần cải thiện là chuẩn hóa tag khi tạo ticket để report về sau chính xác hơn.

## 5. Response / Resolution Time

File export hiện tại không có field thời gian phản hồi hoặc thời gian xử lý chi tiết. Vì vậy, trong báo cáo này em dùng trạng thái ticket, priority và tag/category làm chỉ số chính.

Nếu triển khai tiếp, nên bổ sung các field sau vào export/report:

- Created date
- First response date
- Resolved date
- SLA deadline
- SLA status
- Assigned owner

Các field này sẽ giúp tính được response time, resolution time và SLA compliance chính xác hơn.

## Kết luận report

Từ dữ liệu export, có thể thấy workload chính tập trung vào CRM, LMS, TMS và các vấn đề account/mail. Bước tiếp theo là phân tích pattern để chọn ra nhóm vấn đề có tính lặp lại và có thể giảm tải bằng automation hoặc cải tiến quy trình.
