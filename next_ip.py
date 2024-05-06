import ipaddress

def calculate_next_ip_address(ip_address):
  """Calculates the next IP address.

  Args:
    ip_address: A string representing the IP address.

  Returns:
    A string representing the next IP address.
  """

  ip_address = ipaddress.ip_address(ip_address)
  next_ip_address = ip_address + 1
  return str(next_ip_address)

# Example usage:

ip_address = "10.0.0.2"
next_ip_address = calculate_next_ip_address(ip_address)
print(next_ip_address)

net = ipaddress.ip_network("10.0.0.0/22")

print("broadcast_address: ", net.broadcast_address)
print("network_address: ", net.network_address)
for ip in net.hosts():
    print(type(ip), " -> ", ip)