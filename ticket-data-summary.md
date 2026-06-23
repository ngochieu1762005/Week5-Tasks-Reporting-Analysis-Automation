# Ticket Data Summary

## Nguồn dữ liệu

File này được tổng hợp từ dữ liệu export Odoo trong `sample.xlsx`. Khác với bản demo ban đầu chỉ dùng 6 ticket practice, dữ liệu này có **131 ticket** từ hệ thống Helpdesk, nên phần phân tích bên dưới phản ánh sát thực tế hơn.

Trong file export, ticket được nhóm theo các trạng thái chính:

| Trạng thái trong export | Số lượng ticket |
|---|---:|
| New | 6 |
| First Response Sent | 17 |
| In Progress | 5 |
| Resolved | 91 |
| Cancelled | 12 |
| **Tổng cộng** | **131** |

## Nhận xét nhanh

Phần lớn ticket trong export đã được xử lý xong, với 91 ticket ở trạng thái `Resolved`. Tuy nhiên vẫn còn một nhóm ticket đang ở các trạng thái cần theo dõi như `New`, `First Response Sent` và `In Progress`. Đây là nhóm phù hợp để dùng cho việc phân tích workload và tìm các pattern vận hành.

## Phân bổ theo mức ưu tiên

| Priority | Số lượng | Tỷ lệ |
|---|---:|---:|
| Urgent | 40 | 30.5% |
| High priority | 42 | 32.1% |
| Medium priority | 9 | 6.9% |
| Low priority | 40 | 30.5% |
| **Tổng cộng** | **131** | **100%** |

## Nhận xét về priority

Nhóm `Urgent` và `High priority` chiếm tổng cộng 82/131 ticket, tương đương khoảng 62.6%. Điều này cho thấy workload của team support không chỉ là các request nhỏ lẻ, mà có khá nhiều ticket cần xử lý nhanh hoặc có mức ảnh hưởng cao.

## Phân bổ theo tag chính

| Tag / Nhóm vấn đề | Số lượng ticket |
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

## Một số ticket tiêu biểu

| Ticket ID | Subject | Tag chính | Priority | Trạng thái export |
|---|---|---|---|---|
| 325 | MINDX ĐÀ NẴNG - HỖ TRỢ KIỂM TRA ĐỐI CHIẾU SỐ LƯỢNG ĐỔI QUÀ TRÊN DENISE | E-learning | High priority | New |
| 287 | KHÔNG TẠO MÃ QR THANH TOÁN ĐƯỢC | CRM | High priority | New |
| 296 | SỐ LƯỢNG GIỮA 2 HỆ THỐNG ECOUNT VÀ DENISE KHÔNG THỐNG NHẤT ĐỂ HV đổi quà | LMS | Low priority | New |
| 308 | XIN CẤP LẠI TÀI KHOẢN ECOUNT | User responded | Urgent | First Response Sent |
| 288 | NHỜ TEAM TECH SỬA LẠI TÊN ĐÚNG TRONG PHẦN ENROLLMENT CỦA HỌC VIÊN | CRM | Urgent | First Response Sent |
| 335 | BU DĨ AN-NHỜ HỖ TRỢ FIX LỖI TẠO PHIẾU DROPOUT CHO HV | LMS | High priority | First Response Sent |

## Kết luận

Dữ liệu thật cho thấy các nhóm issue nổi bật là CRM, LMS, TMS, mail/account và một số lỗi liên quan Denise/Ecount/payment. Vì vậy, phần reporting và pattern analysis nên dùng các nhóm này thay vì chỉ dựa trên 6 scenario practice.
