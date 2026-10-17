# File to setup Replit environment
{ pkgs }: {
  deps = with pkgs; [
    (python3.withPackages (
      ps: with pkgs; [
        pygame
        pytest
      ]
    ))
  ];
}
