using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Server.Kestrel.Core;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.AspNetCore.Hosting;


var builder = WebApplication.CreateBuilder(args);

// ===== VULNERABLE CONFIGURATIONS =====
// 1. Debug mode in production
builder.Environment.EnvironmentName = "Development";

// 2. Configure Kestrel directly (correct approach)
builder.WebHost.ConfigureKestrel(options => 
{
    options.AddServerHeader = true; // Server info disclosure
    options.Limits.MaxRequestBodySize = null; // No size limits
});

var app = builder.Build();

// 3. Disable security headers
app.Use(async (context, next) =>
{
    context.Response.Headers.Remove("X-Content-Type-Options");
    await next();
});

app.MapControllers();
app.Run();