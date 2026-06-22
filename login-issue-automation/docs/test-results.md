# Automation Test Results

## 1. Mục tiêu

Test workflow Login Issue Automation để đảm bảo automation xử lý đúng case an toàn và manual review các case rủi ro.

## 2. Test cases

| Test ID | Case | Expected | Status |
|---|---|---|---|
| TC-01 | Login issue + active employee | Resolved by automation | Passed |
| TC-02 | Login issue + terminated employee | Manual review | Passed |
| TC-03 | Login issue + unknown employee | Manual review | Passed |
| TC-04 | Non-login issue | Skipped | Passed |
| TC-05 | Missing requester email | Manual review | Passed |
| TC-06 | Security risk keyword | Manual review | Passed |

## 3. Command

```bash
python -m unittest discover -s tests
```

## 4. Expected output

```text
Ran 6 tests in ...s
OK
```

## 5. Kết luận

Pass rate: 100%.

Workflow đáp ứng safety boundary: chỉ reactivate LMS khi employee status là active. Các case terminated, unknown, missing email hoặc security risk đều được chuyển manual review.
