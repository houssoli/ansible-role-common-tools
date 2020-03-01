export http_proxy='http://proxy_user:proxy_pass@proxy_host:proxy_port'
export https_proxy='http://proxy_user:proxy_pass@proxy_host:proxy_port'

export ftp_proxy=$http_proxy
export rsync_proxy=$http_proxy
 
export no_proxy='127.0.0.1, localhost, 192.168.0.0/16, 172.16.0.0/12, repository'