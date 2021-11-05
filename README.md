## Mô tả

- Mô hình hệ thống mạng nội bộ chỉ có 1 máy được phép ra ngoài internet (máy X).
- Sử dụng Ansible copy source từ máy X (thư mục src) đến các máy khác (remote hosts) trong hệ thống.
- Khi có thay đổi từ source, ansible sẽ move thư mục cũ sang 1 thư mục backup trên remote hosts.

## Hướng dẫn sử dụng

### Roles

- **copy** (tag: copy): sử dụng để copy source từ máy X đến remote hosts.
- **config** (tag: config):  sử dụng để cấu hình các file cần thiết trên remote hosts.

### Run

- `cd` vào thư mục *ansible** và chạy lệnh theo cấu trúc:
```
ansible-playbook -i hosts -l <host_name1>,<host_name2> site.yml --tags=<tag1>,<tag2> --skip-tags=<tag1>,<tag2>
```
- Trong đó:
  - `-l <host_name>`: chạy trên 1 remote host cụ thể, có thể bỏ nếu cần chạy tất cả.
  - `--tags=<tag>`: chỉ định chạy roles cụ thể, bỏ nếu cần chạy tất cả roles.
  - `--skip-tags=<tag>`: chỉ định bỏ qua roles cụ thể, bỏ nếu k cần thiết.
  - **tag** khả dụng: copy, config.
  - `-i hosts`: chỉ định  inventory host list nằm trong file *hosts*
  - `site.yml`: file playbook