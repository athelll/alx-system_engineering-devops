# This class edits the ssh config file
class 'ssh' {
  client::password_authentication => 'no',
  client::pubkey_authentication => 'yes',
  client::identity_file => '~/.ssh/school',
}
