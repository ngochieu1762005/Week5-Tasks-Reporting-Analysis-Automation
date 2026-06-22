# Week 5 - Phân tích Pattern Ticket

## 1. Mục tiêu

Phân tích dữ liệu Week 4 để xác định recurring issues, impact, root cause ban đầu và automation opportunity.

## 2. Tổng quan dữ liệu

| Chỉ số | Giá trị |
|---|---:|
| Tổng ticket | 6 |
| Ticket solved | 6 |
| LMS Technical Issues | 4 |
| Reporting / Business Requests | 2 |
| Users affected tối thiểu | 78+ |

## 3. Pattern chính

Pattern lớn nhất là **LMS Technical Issues**, bao gồm:

- Login / Account Access
- Performance
- Submission Bug
- Video Playback

Nhóm này chiếm 66.7% dữ liệu, cho thấy LMS cần được ưu tiên theo dõi trong vận hành.

## 4. Top issues / important patterns

| Rank | Issue / Pattern | Ticket liên quan | Users affected | Impact | Priority |
|---:|---|---|---:|---|---|
| 1 | LMS Technical Issues | 00001, 00002, 00003, 00005 | 78+ | Ảnh hưởng trực tiếp tới học tập/vận hành | High |
| 2 | Critical Submission Bug | 00003 | 50+ | Không nộp được final exam | Critical |
| 3 | Performance Issue | 00002 | 15 | Cả lớp bị chậm LMS | High |
| 4 | Video Playback Issue | 00005 | 12 | Không xem được bài học | High |
| 5 | Login Issue | 00001 | 1 | Teacher không truy cập được LMS | Medium |
| 6 | Reporting / Business Request | 00004, 00006 | N/A | Yêu cầu nghiệp vụ/báo cáo | Medium |

## 5. Top 3 recurring/problem candidates for root cause analysis

| Rank | Selected Issue | Root cause có thể | Evidence | Recommendation |
|---:|---|---|---|---|
| 1 | Login Issue | Account inactive/disabled sau thời gian không hoạt động | Ticket 00001, workflow xử lý rõ ràng | Automate account reactivation sau khi check HR |
| 2 | Performance Issue | High load, slow API, database query chậm | 15 users affected | Thêm monitoring checklist và alert |
| 3 | Critical Submission Bug | Lỗi upload/submission validation hoặc backend logic | 50+ users affected | Escalate dev team, có emergency process |

## 6. Impact analysis

| Ticket | Users affected | Business impact | Team time cost estimate |
|---|---:|---|---|
| Critical LMS Submission Bug | 50+ | Ảnh hưởng final exam submission | Cao, cần escalation |
| LMS Performance Issue | 15 | Ảnh hưởng cả lớp | Trung bình/cao |
| LMS Video Playback Issue | 12 | Ảnh hưởng lesson delivery | Trung bình |
| LMS Login Issue | 1 | Teacher không truy cập LMS | 5-10 phút/ticket nếu xử lý thủ công |
| Feature Request | N/A | Product/business improvement | Cần review requirement |
| Fixed Deadline Request | N/A | Có deadline trước 09:00 | Cần xử lý đúng hạn |

## 7. Root cause ban đầu

| Issue | Root cause có thể | Evidence | Hướng xử lý |
|---|---|---|---|
| Login Issue | Account locked/disabled/inactive | User không login được | Check HR, reactivate nếu active |
| Performance Issue | Load cao, slow DB/API, infrastructure | 15 users bị ảnh hưởng | Azure/App Insights, logs, metrics |
| Submission Bug | Backend/upload validation lỗi | 50+ users affected | Escalate dev team |
| Video Playback | CDN/file/permission/network | 12 users affected | Kiểm tra video asset/CDN |
| Feature Request | Nhu cầu nghiệp vụ mới | Request PDF report | Product review |
| Fixed Deadline | Báo cáo cần trước mốc giờ | Deadline 09:00 | Time-driven handling |

## 8. Automation opportunity assessment

| Issue | Automation suitability | Lý do |
|---|---|---|
| Login Issue | Cao | Logic rõ: detect login, check HR, active thì reactivate, còn lại manual review |
| Performance Issue | Trung bình | Có thể automate monitoring/alert, nhưng root cause cần điều tra |
| Critical Submission Bug | Thấp | Impact cao, không nên tự fix bằng automation |
| Video Playback Issue | Trung bình | Có thể automate health check, fix cần điều tra |
| Feature Request | Thấp | Cần business/product decision |
| Fixed Deadline Request | Thấp | Phụ thuộc scope và deadline |

## 9. Selected automation candidate

**Selected issue:** Scenario 1 - Login Issue / Account Reactivation

Lý do chọn:

- Có khả năng lặp lại trong vận hành thực tế.
- Manual fix rõ ràng và lặp lại.
- Có thể nhận diện bằng keyword.
- Có thể check employee status trước khi hành động.
- Có boundary an toàn: chỉ reactivate khi employee active.
- Các case terminated/unknown/error sẽ manual review.
- Phù hợp Operating Engineer approach.

## 10. Kết luận

LMS Technical Issues là nhóm nổi bật nhất. Critical Submission Bug có impact cao nhất nhưng cần dev team xử lý. Login Issue là automation candidate tốt nhất vì có workflow rõ ràng, có thể tự động hóa an toàn và giúp giảm workload support.
