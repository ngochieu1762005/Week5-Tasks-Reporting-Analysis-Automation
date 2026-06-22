# Automation Test Results

## 1. Mục tiêu

Test workflow Login Issue Automation để đảm bảo automation xử lý đúng case an toàn và chuyển các case rủi ro sang manual review.

Bộ test đã được mở rộng để dùng email nội bộ dạng `@mindx.com` và nhiều trạng thái HR hơn, thay vì chỉ có `active`, `terminated`, `unknown` như bản demo ban đầu.

## 2. Test cases

| Test ID | Case | Email test | Expected | Status |
|---|---|---|---|---|
| TC-01 | Login issue + active employee | `teacher01@mindx.com` | Resolved by automation | Passed |
| TC-02 | Login issue + terminated employee | `terminated.teacher@mindx.com` | Manual review | Passed |
| TC-03 | Login issue + unknown employee | `unknown.user@mindx.com` | Manual review | Passed |
| TC-04 | Login issue + locked employee | `locked.user@mindx.com` | Manual review | Passed |
| TC-05 | Login issue + suspended employee | `suspended.user@mindx.com` | Manual review | Passed |
| TC-06 | Login issue + contractor account | `contractor01@mindx.com` | Manual review | Passed |
| TC-07 | Non-login issue | `teacher02@mindx.com` | Skipped | Passed |
| TC-08 | Missing requester email | `None` | Manual review | Passed |
| TC-09 | Security risk keyword | `teacher01@mindx.com` | Manual review | Passed |

## 3. Command

```bash
python -m unittest discover -s tests
```

## 4. Expected output

```text
Ran 9 tests in ...s
OK
```

## 5. Kết luận

Pass rate: 100%.

Workflow đáp ứng safety boundary: chỉ reactivate LMS khi employee status là `active`. Các trạng thái khác như `terminated`, `unknown`, `locked`, `suspended`, `contractor`, thiếu email hoặc có dấu hiệu security risk đều được chuyển sang manual review.
